# Average Down calculator.
# Display graph. 

import matplotlib.pyplot as plt

def calc(total_cost, total_shares):

    print("Enter Number of Shares & Price Per Share For First & Second Purchase.")

    for i in range(1, 3):

        shares = int(input("\nEnter Share Amount: "))
        price = float(input("Enter Price: $ "))

        cost = shares * price

        total_cost += cost 
        total_shares += shares
 
        bar_labels.append('Purchase ' + str(i) + ': ' + str("{:,}".format(shares)) + ' Shares @ $' + str("{:,.2f}".format(price)))
        heights.append(price)

    # Calculate average down 
    avg_down = total_cost / total_shares

    heights.append(avg_down)
    bar_labels.append('Average Down: ' + str("{:,}".format(total_shares)) + ' Shares @ $' + str("{:,.2f}".format(avg_down)))

    print("\nResults")
    print("\nTotal Shares:", total_shares)
    print("Total Cost: ${:,.2f}".format(total_cost))
    print("Average Down Price @ " + str(total_shares) + " Shares: ${:,.2f}".format(avg_down))

    graph(bar_labels, heights)

def graph(w, z):

    plt.bar(bar_labels, heights) 

    plt.title("Bar Graph")
    plt.show()

x = 0
y = 0
bar_labels = []
heights = []

calc(x, y)

