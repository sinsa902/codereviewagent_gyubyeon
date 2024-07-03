#include "pch.h"
#include "../Project6/ALU.cpp";
#include "../Project6/Result.cpp";

TEST(ALU, ADDTest) {
	ALU alu;
	alu.setOperand1(10);
	alu.setOperand2(20);
	alu.setOPCODE("ADD");

	Result ret;
	alu.enableSignal(&ret);

	EXPECT_EQ(30, ret.getResult());
	EXPECT_EQ(0, ret.getStatus());
}
