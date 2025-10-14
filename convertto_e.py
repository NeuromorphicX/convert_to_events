from v2e import V2E

cfg = dict(
    input_video="baby_1.mp4",
    output_folder="baby_1_v2e",
    pos_threshold=0.2,
    neg_threshold=0.2,
    sigma_threshold_noise=0.03,
    refractory_period=1e-4,
    timestamp_resolution=1e-6,
    dvs128=True,
    output_events_file="events.h5",
    save_td=True
)
V2E(**cfg).run()
