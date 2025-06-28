from celery import shared_task

@shared_task
def test_celery():
    print('celery works')
    return 'Success'
