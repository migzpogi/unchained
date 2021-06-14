package main

import(
	"fmt"
	"example.com/greetings"
)

func main(){
	message := greetings.Hello("Miguel")
	fmt.Println(message)
}