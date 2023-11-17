package code.java.stock;


// 订阅者接口
interface Subscriber {
    void update(String message);
}

// 股票类
class Stock {
    private String symbol;
    private double price;

    public Stock(String symbol, double price) {
        this.symbol = symbol;
        this.price = price;
    }

    // 更新股票价格的方法
    public void setPrice(double price) {
        this.price = price;
        // 股票价格变动后，将通知发送到观察者
        StockObserver.notify(this.symbol, "Price updated to " + price);
    }

    // 其他股票相关方法...
}

