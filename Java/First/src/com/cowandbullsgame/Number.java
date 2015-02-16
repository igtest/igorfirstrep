package com.cowandbullsgame;

abstract public class Number {
    protected static final int DEFAULT_AMOUNT = 4;

    public int[] bufComp = new int[DEFAULT_AMOUNT];

    abstract public void setValue();

    abstract public void getValue();
}
