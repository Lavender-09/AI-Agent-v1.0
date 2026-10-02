/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

import java.io.Serializable;

public class Fruit implements Serializable{
    private String fruit;
    private int quantity;
    private double price;
    
    public Fruit(String fruit, int quantity, double price){
        this.fruit = fruit;
        this.quantity = quantity;
        this.price = price;
    }
    
    public String getFruit(){return fruit;}
    public int getQuantity(){return quantity;}
    public double getPrice(){return price;}
    
    public void setFruit(String fruit){this.fruit = fruit;}
    public void setQuantity(int quantity){this.quantity = quantity;}
    public void setPrice(double price){this.price = price;}
}
