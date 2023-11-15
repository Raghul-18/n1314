import os

pipe_read, pipe_write = os.pipe()

pid = os.fork()

if pid == 0:
    os.close(pipe_write)  
    child_data = os.read(pipe_read, 1024)
    print(f"Child received: {child_data.decode()}")
else:
    os.close(pipe_read) 
    data_to_send = "Hello from Parent!"
    os.write(pipe_write, data_to_send.encode())
    os.wait() 


pipe1_read, pipe1_write = os.pipe()
pipe2_read, pipe2_write = os.pipe()

pid2 = os.fork()

if pid2 == 0:
    os.close(pipe1_read) 
    os.close(pipe2_write) 
    data_to_send2 = "Hello from Parent 2 to Child 11!"
    os.write(pipe1_write, data_to_send2.encode())
    os._exit(0)  
else:
    pid1 = os.fork()

    if pid1 == 0:
        os.close(pipe2_read) 
        os.close(pipe1_write)
        data_to_send1 = "Hello from Parent 1 to Child 21!"
        os.write(pipe2_write, data_to_send1.encode())
        os._exit(0) 
    else:
        os.waitpid(pid1, 0)
        os.waitpid(pid2, 0)
        message_from_child1 = os.read(pipe1_read, 1024).decode()
        message_from_child2 = os.read(pipe2_read, 1024).decode()
        print(message_from_child1)
        print(message_from_child2)

