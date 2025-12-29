package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
)

const RequiredNumberOfArguments = 4
const MinNumberOfArguments = 1
const FloatBitSize = 64

func GetCoeffA() float64 {
	for {
		fmt.Print("Enter coefficient a: ")
		var coeffA string
		fmt.Scan(&coeffA)

		a, err := strconv.ParseFloat(coeffA, FloatBitSize)
		if err != nil {
			fmt.Println("Incorrect coeffinient A entered. Please try again")
		} else {
			return a
		}
	}
}

func GetCoeffB() float64 {
	for {
		fmt.Print("Enter coefficient b: ")
		var coeffB string
		fmt.Scan(&coeffB)

		b, err := strconv.ParseFloat(coeffB, FloatBitSize)
		if err != nil {
			fmt.Println("Incorrect coefficient B. Please try again")
		} else {
			return b
		}
	}
}

func GetCoeffC() float64 {
	for {
		fmt.Print("Enter coefficient c: ")
		var coeffC string
		fmt.Scan(&coeffC)

		c, err := strconv.ParseFloat(coeffC, FloatBitSize)
		if err != nil {
			fmt.Println("Incorrect coefficient C. Please try again")
		} else {
			return c
		}
	}
}

func CheckCorrectnessCoeffFromArg(rawCoeff, coeffName string) float64 {

	coeff, err := strconv.ParseFloat(rawCoeff, FloatBitSize)
	if err == nil {
		return coeff
	} else {
		for {
			fmt.Printf("Incorrect coefficient %s. Please try again", coeffName)
			fmt.Println()

			fmt.Printf("Enter coefficient %s: ", coeffName)
			var coeff string
			fmt.Scan(&coeff)

			finalCoeff, err := strconv.ParseFloat(coeff, FloatBitSize)
			if err == nil {
				return finalCoeff
			}
		}
	}
}

func ShowAllCoeff(a, b, c float64) {
	fmt.Println("Entered coefficients:")
	fmt.Println()
	fmt.Printf("a = %f", a)
	fmt.Println()
	fmt.Printf("b = %f", b)
	fmt.Println()
	fmt.Printf("c = %f", c)
	fmt.Println()
	fmt.Println()
}

func CalculateRoots(a, b, c float64) {
	ShowAllCoeff(a, b, c)

	discriminant := math.Pow(b, 2) - 4*a*c

	var roots []float64

	if discriminant < 0 {
		fmt.Println("No roots found")
		os.Exit(0)
	} else {
		root1 := (-b + math.Sqrt(discriminant)) / (2 * a)
		roots = append(roots, root1)
		root2 := (-b - math.Sqrt(discriminant)) / (2 * a)

		if root1 != root2 {
			roots = append(roots, root2)
		}
		fmt.Println("fonuded roots ---", roots)
	}
}

func CalculateWithUserEnter() {
	a := GetCoeffA()
	b := GetCoeffB()
	c := GetCoeffC()

	CalculateRoots(a, b, c)
}

func main() {
	if len(os.Args) > 4 {
		fmt.Println("Too many arguments entered")
		fmt.Println()
		CalculateWithUserEnter()

	} else if len(os.Args) < 4 {
		fmt.Println("Too few arguments entered")
		fmt.Println()
		CalculateWithUserEnter()

	} else {
		a := CheckCorrectnessCoeffFromArg(os.Args[1], "A")
		b := CheckCorrectnessCoeffFromArg(os.Args[2], "B")
		c := CheckCorrectnessCoeffFromArg(os.Args[3], "C")

		CalculateRoots(a, b, c)
	}
}
