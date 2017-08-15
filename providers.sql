DROP DATABASE IF EXISTS providers;
CREATE DATABASE providers;

\c providers;

CREATE TABLE providers
(
    drg_definition text COLLATE pg_catalog."default",
    provider_id text COLLATE pg_catalog."default",
    provider_name text COLLATE pg_catalog."default",
    provider_street_address text COLLATE pg_catalog."default",
    provider_city text COLLATE pg_catalog."default",
    provider_state text COLLATE pg_catalog."default",
    provider_zip_code text COLLATE pg_catalog."default",
    hospital_referral_region_description text COLLATE pg_catalog."default",
    total_discharges text COLLATE pg_catalog."default",
    average_covered_charges text COLLATE pg_catalog."default",
    average_total_payments text COLLATE pg_catalog."default",
    average_medicare_payments text COLLATE pg_catalog."default"
)
WITH (
    OIDS = FALSE
);

