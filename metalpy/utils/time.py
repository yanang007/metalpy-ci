import time


class Timer:
    def __init__(self):
        self.started = 0
        self.elapsed = 0
        pass

    def __enter__(self):
        self.started = time.perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stopped = time.perf_counter()
        self.elapsed = self.stopped - self.started

    def __str__(self):
        elapsed_mins, elapsed_secs, elapsed_milis = perf_epoch_time(self.started, self.stopped)
        if elapsed_mins > 0:
            return f"{elapsed_mins} min {elapsed_secs} s"
        elif elapsed_secs > 0:
            return f"{elapsed_secs} s {elapsed_milis} ms"
        else:
            return f"{elapsed_milis} ms"


def epoch_time(start_time, end_time):
    elapsed_time = end_time - start_time
    elapsed_mins = int(elapsed_time / 60)
    elapsed_secs = int(elapsed_time - (elapsed_mins * 60))
    return elapsed_mins, elapsed_secs


def perf_epoch_time(start_time, end_time):
    elapsed_time = end_time - start_time
    elapsed_milis = elapsed_time / 1000
    elapsed_secs = int(elapsed_milis / 1000)
    elapsed_mins = int(elapsed_secs / 60)

    elapsed_milis -= elapsed_secs * 1000
    elapsed_secs -= elapsed_mins * 60

    return elapsed_mins, elapsed_secs, elapsed_milis
