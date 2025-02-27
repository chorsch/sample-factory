from sample_factory.launcher.launcher_utils import seeds
from sample_factory.launcher.run_description import Experiment, ParamGrid, RunDescription

_params = ParamGrid(
    [
        ("seed", [0]),
        ("num_contexts", [5]),
    ]
)

_experiment = Experiment(
    "doom_battle_contexts",
    "python -m sf_examples.vizdoom.enjoy_contextual_vizdoom --save_every_sec=120 --with_wandb=True --env=doom_battle_contexts --train_for_env_steps=1000000000 --algo=APPO --env_frameskip=4 --use_rnn=True --wide_aspect_ratio=False --num_workers=20 --num_envs_per_worker=16 --decorrelate_envs_on_one_worker=False --max_pure_expl_steps=200 --num_policies=2 --no_render --save_video --video_frames=-1 --max_num_episodes=1 --policy_index=1",
    _params.generate_params(randomize=False),
)

RUN_DESCRIPTION = RunDescription("doom_battle_contexts", experiments=[_experiment])

# --with_wandb=True
# run:
# python -m sample_factory.launcher.run --run=sf_examples.vizdoom.experiments.doom_basic --backend=processes --num_gpus=1 --max_parallel=2  --pause_between=0 --experiments_per_gpu=2
