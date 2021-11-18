start_text = 'Welcome {first_name}! Use "`/subscribe node_id network`"' \
             ' to receive status updates about a node.\n' \
             'For example: `/subscribe 3Te6Gty9l7L1CABbo+Qw9NT5aa0b6KOkC3NiwIVaGkwC canary`'

already_started_text = "You have started the bot already."

node_status_text = "{emoji}{emoji}{emoji}\n" \
                   "Node status has changed: {status}\n" \
                   "Node ID: {node_id}"

node_subscribe_text = "You have successfully subscribed to the node. \nCurrent node status: {}"

node_already_subscribed_text = "You are already subscribed to this node."

node_unsubscribe_text = "You have successfully unsubscribed from the node."

node_already_unsubscribed_text = "You are already unsubscribed from this node."

node_does_not_exist_text = "Node does not exist. Please, insert a valid Node ID and network."

invalid_subscription_format_text = 'Invalid format. Please, insert a valid Node ID and network (canary or mainnet).'

list_nodes_line_text = "###\n" \
                       "Node ID: {node_id}\n" \
                       "Network: {network}net\n" \
                       "Status: {status}\n" \
                       "###\n"

list_nodes_no_nodes_text = "You aren't registered to any nodes."
