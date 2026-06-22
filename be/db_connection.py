SUPABASE_URL="https://ncsacgcpxorhgysxtxmr.supabase.co"
SUPABASE_KEY="sb_publishable_e7Occ6cRAsTKEuhYWeT5cA_joVKQoA_ "

# pip install supabase
from supabase import create_client

supabase_client_object=create_client(
   SUPABASE_URL,
    SUPABASE_KEY
)
