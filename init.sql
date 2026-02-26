--
-- PostgreSQL database cluster dump
--

\restrict yva3s9sCsOJuKROzKbg6YcO4rbErpwU3bdRDGhFnbiL8B7BY033wVuFTQobHNsG

SET default_transaction_read_only = off;

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

--
-- Roles
--

CREATE ROLE postgres;
ALTER ROLE postgres WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS;

--
-- User Configurations
--








\unrestrict yva3s9sCsOJuKROzKbg6YcO4rbErpwU3bdRDGhFnbiL8B7BY033wVuFTQobHNsG

--
-- Databases
--

--
-- Database "template1" dump
--

\connect template1

--
-- PostgreSQL database dump
--

\restrict cwcxLe70jLGi0AgW7RA7RL2FptRRJ8QHL6HFooaVuufK7nB1kp0Xzs9K7dfUchR

-- Dumped from database version 18.2 (Debian 18.2-1.pgdg13+1)
-- Dumped by pg_dump version 18.2 (Debian 18.2-1.pgdg13+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- PostgreSQL database dump complete
--

\unrestrict cwcxLe70jLGi0AgW7RA7RL2FptRRJ8QHL6HFooaVuufK7nB1kp0Xzs9K7dfUchR

--
-- Database "postgres" dump
--

\connect postgres

--
-- PostgreSQL database dump
--

\restrict thSkmSwoeQrCwvnNVKyAQDT6iOr67OQPywYK2c1C1M2YchJv4UvRvWowlkwnIwd

-- Dumped from database version 18.2 (Debian 18.2-1.pgdg13+1)
-- Dumped by pg_dump version 18.2 (Debian 18.2-1.pgdg13+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: jobs; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jobs (
    job_id integer NOT NULL,
    user_id integer NOT NULL,
    is_recurring boolean NOT NULL,
    "interval" character varying(45) NOT NULL,
    max_retry_count integer NOT NULL,
    created_time integer NOT NULL
);


ALTER TABLE public.jobs OWNER TO postgres;

--
-- Name: jobs_job_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.jobs_job_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.jobs_job_id_seq OWNER TO postgres;

--
-- Name: jobs_job_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.jobs_job_id_seq OWNED BY public.jobs.job_id;


--
-- Name: task_history; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.task_history (
    job_id integer NOT NULL,
    execution_time integer NOT NULL,
    status character varying(45) NOT NULL,
    retry_count integer NOT NULL,
    last_update_time integer NOT NULL
);


ALTER TABLE public.task_history OWNER TO postgres;

--
-- Name: task_schedule; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.task_schedule (
    next_execution_time integer NOT NULL,
    job_id integer NOT NULL
);


ALTER TABLE public.task_schedule OWNER TO postgres;

--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    username character varying(45) NOT NULL,
    user_email character varying(45) NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_user_id_seq OWNER TO postgres;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: jobs job_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jobs ALTER COLUMN job_id SET DEFAULT nextval('public.jobs_job_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Data for Name: jobs; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jobs (job_id, user_id, is_recurring, "interval", max_retry_count, created_time) FROM stdin;
\.


--
-- Data for Name: task_history; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.task_history (job_id, execution_time, status, retry_count, last_update_time) FROM stdin;
\.


--
-- Data for Name: task_schedule; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.task_schedule (next_execution_time, job_id) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (user_id, username, user_email) FROM stdin;
\.


--
-- Name: jobs_job_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.jobs_job_id_seq', 1, false);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_user_id_seq', 1, false);


--
-- Name: jobs jobs_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jobs
    ADD CONSTRAINT jobs_pkey PRIMARY KEY (job_id);


--
-- Name: task_history task_history_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.task_history
    ADD CONSTRAINT task_history_pkey PRIMARY KEY (job_id);


--
-- Name: task_schedule task_schedule_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.task_schedule
    ADD CONSTRAINT task_schedule_pkey PRIMARY KEY (job_id, next_execution_time);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- PostgreSQL database dump complete
--

\unrestrict thSkmSwoeQrCwvnNVKyAQDT6iOr67OQPywYK2c1C1M2YchJv4UvRvWowlkwnIwd

--
-- PostgreSQL database cluster dump complete
--