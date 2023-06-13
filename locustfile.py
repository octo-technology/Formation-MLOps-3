from locust import FastHttpUser, between, task

YOUR_COOKIE = '...'


class QuickstartUser(FastHttpUser):
    wait_time = between(1, 5)

    @task
    def call_health_route(self):
        self.client.get("/health",
                        headers={"Cookie": YOUR_COOKIE})
