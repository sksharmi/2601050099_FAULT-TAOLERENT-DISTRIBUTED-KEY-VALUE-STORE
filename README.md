1. Open Linux Terminal

If you are using Ubuntu:

Ctrl + Alt + T

First check:

uname -a

Then:

lsb_release -a

You should see your Linux/Ubuntu version.

2. Install required tools

Run:

sudo apt update

Then:

sudo apt install git curl build-essential htop sysstat -y

Install Go:

sudo apt install golang-go -y

Check:

go version

and:

git --version

You should get something like:

go version go1.xx.x linux/amd64
git version 2.xx.x
3. Create your project

Create a folder:

mkdir fault-tolerant-kv
cd fault-tolerant-kv

Check:

pwd

Then initialize Go:

go mod init fault-tolerant-kv
4. Create the basic project structure

Run:

mkdir -p cmd/server internal/kv internal/raft internal/storage
mkdir -p docs benchmarks scripts

Now:

touch README.md

Your project will look like:

fault-tolerant-kv/
│
├── cmd/
│   └── server/
│
├── internal/
│   ├── kv/
│   ├── raft/
│   └── storage/
│
├── benchmarks/
├── scripts/
├── docs/
├── README.md
└── go.mod

Don't worry if this looks big. We'll fill these folders one by one.

5. First make a VERY simple KV store

Before implementing distributed systems, first understand the basic key-value operation.

Create:

nano cmd/server/main.go

Put:

package main

import "fmt"

func main() {
    store := make(map[string]string)

    store["name"] = "Sharmi"
    store["course"] = "MTech CSE"

    fmt.Println("Name:", store["name"])
    fmt.Println("Course:", store["course"])
}

Save:

Ctrl + O → Enter → Ctrl + X

Run:

go run cmd/server/main.go

Output:

Name: Sharmi
Course: MTech CSE

🎯 This is your first working component.

6. Now do the Linux profiling baseline

This is specifically mentioned in your milestone:

Linux profiling baseline established

First run:

/usr/bin/time -v go run cmd/server/main.go

You'll get information such as:

User time
System time
Maximum resident set size
Elapsed time

You can also monitor the system using:

top

or:

htop

For CPU/memory statistics:

vmstat 1 5

For CPU information:

mpstat 1 5

These results become your baseline measurements.

7. Initialize Git

Inside the project:

git init

Then:

git status

Create .gitignore:

nano .gitignore

Add:

bin/
*.log
*.tmp

Then:

git add .

Commit:

git commit -m "Initial project scaffold"
