from locust import FastHttpUser, between, task

YOUR_COOKIE = 'jupyterhub-user-admin=2|1:0|10:1686666827|21:jupyterhub-user-admin|40:N1c0MmQ1S2pqRWQ0SExINEVzVHRnd0d4RVZqck9Q|b18b1798b1e23791e8dbbd60177b2f3ba13fd0df975e3496849697b710a813a3; jupyterhub-session-id=9fbc7ba551b24d238552e3a93ed17e0e; Pycharm-43de7e6c=177a08dc-092a-416d-8b2d-75a6e35a7f47; _ga=GA1.1.606690807.1674053591; _xsrf=2|633f1469|c09fc794dfcef7b2de3b79bf7c586c42|1682257040; ajs_user_id=b78a22e4-4a42-530a-b55f-45a73db96cae; ajs_anonymous_id=3f1bc073-dab4-4ea6-a68b-d4c63855d0d0; Pycharm-43de822b=1c2a0e88-4c6b-43fa-9a44-874e33d0871a; session=86c2c48e-eef3-4f66-8a2c-e0e5eec895db.2Uya1qoXRHeGUS4qvNPASZwA8lA'


class QuickstartUser(FastHttpUser):
    wait_time = between(1, 5)

    @task
    def call_health_route(self):
        self.client.get("/health",
                        headers={"Cookie": YOUR_COOKIE})
