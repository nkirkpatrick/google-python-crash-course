def retry_test(operation, attempts):
  for n in range(attempts):
    if operation():
      print("Attempt " + str(n) + " succeeded")
      break
    else:
      print("Attempt " + str(n) + " failed")

#retry_test(create_user, 3)
#retry(stop_service, 5)