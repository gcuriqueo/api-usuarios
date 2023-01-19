CREATE TABLE public.users (
	id uuid NOT NULL,
	name varchar NULL,
	email varchar NOT NULL,
	"password" varchar NULL,
	phones varchar NULL,
	created timestamp NULL,
	modified timestamp NULL,
	last_login timestamp NULL,
	is_active bool NULL DEFAULT true,
	"token" varchar NULL,
	CONSTRAINT users_pkey PRIMARY KEY (id)
);
CREATE UNIQUE INDEX ix_users_email ON public.users USING btree (email);