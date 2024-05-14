import os
import csv
from stable_baselines3.common.callbacks import BaseCallback

class TrainingRewardCallback(BaseCallback):
    def __init__(self, check_freq: int, log_dir: str, verbose=1):
        super().__init__(verbose)
        self.check_freq = check_freq
        self.log_dir = log_dir
        self.save_path = os.path.join(log_dir, 'Baselines_Output.csv')
        self.best_mean_reward = -float('inf')
        self.csv_file = None
        self.writer = None

    def _init_writer(self):
        self.csv_file = open(self.save_path, 'w', newline='')
        self.writer = csv.writer(self.csv_file)
        self.writer.writerow(['step', 'mean_reward'])

    def _on_training_start(self):
        self._init_writer()

    def _on_step(self):
        if self.n_calls % self.check_freq == 0:
            # Assume `self.logger` is a logger used to store metrics
            x, y = self.n_calls, self.logger.get_loggable_metrics()
            self.writer.writerow([x, y['reward']])
            if y['reward'] > self.best_mean_reward:
                self.best_mean_reward = y['reward']

        return True

    def _on_training_end(self):
        if self.csv_file:
            self.csv_file.close()
