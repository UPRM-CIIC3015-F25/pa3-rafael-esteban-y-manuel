from Cards.Card import Card, Rank
from collections import Counter

# TODO (TASK 3): Implement a function that evaluates a player's poker hand.
#   Loop through all cards in the given 'hand' list and collect their ranks and suits.
#   Use a dictionary to count how many times each rank appears to detect pairs, three of a kind, or four of a kind.
#   Sort these counts from largest to smallest. Use another dictionary to count how many times each suit appears to check
#   for a flush (5 or more cards of the same suit). Remove duplicate ranks and sort them to detect a
#   straight (5 cards in a row). Remember that the Ace (rank 14) can also count as 1 when checking for a straight.
#   If both a straight and a flush occur in the same suit, return "Straight Flush". Otherwise, use the rank counts
#   and flags to determine if the hand is: "Four of a Kind", "Full House", "Flush", "Straight", "Three of a Kind",
#   "Two Pair", "One Pair", or "High Card". Return a string with the correct hand type at the end.
def evaluate_hand(hand: list[Card]):
    if not hand:
        return "High Card"

# count ranks and suits using counter function in the collections library.
    ranks = [card.rank.value for card in hand]
    suits = [card.suit for card in hand]

    rank_counts = Counter(ranks)
    suit_counts = Counter(suits)

    #verify flush if count is equal to 5, it assigns it the value of flush_suit, else the value is set to None.
    flush_suit = None
    for suit, count in suit_counts.items():
        if count >= 5:
            flush_suit = suit
            break
    is_flush = flush_suit is not None

   # verify straight
    unique_ranks = sorted(set(ranks))
    # Consider aces as one too
    if 14 in unique_ranks:
        unique_ranks.append(1)
    is_straight = False
    straight_high = None
    for i in range(len(unique_ranks) - 4):
        if unique_ranks[i + 4] - unique_ranks[i] == 4:
            is_straight = True
            straight_high = unique_ranks[i + 4]
    # Straight flush
    if is_flush:
        suited_cards = [card.rank.value for card in hand if card.suit == flush_suit]
        suited_ranks = sorted(set(suited_cards))
        if 14 in suited_ranks:
            suited_ranks.append(1)
        for i in range(len(suited_ranks) - 4):
            if suited_ranks[i + 4] - suited_ranks[i] == 4:
                return "Straight Flush"

    # --- Rank counts ---
    counts = sorted(rank_counts.values(), reverse=True)
    if counts[0] == 4:
        return "Four of a Kind"
    #if counts[0] == 3 and counts[1] >= 2:
    #   return "Full House"
    if is_flush:
        return "Flush"
    if is_straight:
        return "Straight"
    if counts[0] == 3:
        return "Three of a Kind"
    if counts[0] == 3 and counts[1] >= 2:
     return "Full House"
    if counts[0] == 2:
        return "0ne Pair"
    if counts[0] == 2 and counts[1] == 2:
        return "Two Pair"

    return "High Card" # If none of the above, it's High Card
