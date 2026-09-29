package main

import "fmt"

func main() {
    store := make(map[string]string)

    store["name"] = "Sharmi"
    store["course"] = "MTech CSE"

    fmt.Println("Name:", store["name"])
    fmt.Println("Course:", store["course"])
}