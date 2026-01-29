import os

# Local development defaults
os.environ.setdefault(
    "DATABASE_URL",
    "postgresql://neondb_owner:npg_ro53mHgbtXfi@ep-plain-wildflower-agogn39r.c-2.eu-central-1.aws.neon.tech/mardi_vest_aloha_521023",
)
os.environ.setdefault("SECRET_KEY", "Mlkj1929!")