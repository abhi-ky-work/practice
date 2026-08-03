// 1. Problem Statement:
// "Design and write a thread-safe MoneyTransferService class.
// You have a Wallet object with a balance. You need a method transfer(sourceWalletId, targetWalletId, amount).
// Constraint: Millions of transfers happen simultaneously. Ensure that:
// No deadlocks occur (e.g., User A transfers to B, while B transfers to A).
// Money is never created or destroyed (Atomicity).
// You cannot use a database for this exercise; do it in-memory using language primitives (Java synchronized or ReentrantLock).”


// check if source wallet is active, and amount is present
// check if target wallet is active and current balance
// create a key for the transactionId : srcId-trnsId-amnt-timestamp-uuid
// check if the deadlock key pattern exist or not on system ( *trgtId* , *srcId* ), if exists prevent creating transactionId
// paymentTransaction(){} : returns the balance of targetwallet or check the total sum of the wallets 
// if Post transaction validation is ok : success ? raiseFlag
// bAccBalance : 
// =====
function sourceWalletDetails(){
return {
isActive : "true",
balance : 100,
}
}

function targetWalletDetails(){
return {
isActive : "true",
balance : 100,
}
}

function createTransactionId( srcId, trnsId, amount ){

return {
transactionId : srcId-trnsId-amnt-timestamp,
status : inProcess,
deadLock : true, // if transactionId  
errMsg : ""
}
}



function transfer(sourceWalletId, targetWalletId, amount){
}
