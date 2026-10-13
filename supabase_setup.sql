-- Run in Supabase SQL Editor. Never expose the service-role key to Streamlit users.
create table if not exists public.user_settings (
    user_id uuid primary key references auth.users(id) on delete cascade,
    default_sheet_url text,
    google_refresh_token_encrypted text,
    updated_at timestamptz not null default now()
);
alter table public.user_settings enable row level security;
create policy "Users read own settings" on public.user_settings
for select to authenticated using ((select auth.uid()) = user_id);
create policy "Users insert own settings" on public.user_settings
for insert to authenticated with check ((select auth.uid()) = user_id);
create policy "Users update own settings" on public.user_settings
for update to authenticated using ((select auth.uid()) = user_id)
with check ((select auth.uid()) = user_id);
