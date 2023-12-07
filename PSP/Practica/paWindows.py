def esWindows():
  try:
    sys.getwindowsversion()
  except AttributeError:
    return (False)
  else:
    return (True)
  

  if esWindows():
  subprocess.check_output("wmic process where processid=\""+str(os.getpid())+"\" CALL   setpriority \"below normal\"") 
else:
  os.nice(1)