package main

type Job struct {
	job_id          int
	user_id         int
	is_recurring    bool
	interval        string
	max_retry_count int
	created_time    int
}
