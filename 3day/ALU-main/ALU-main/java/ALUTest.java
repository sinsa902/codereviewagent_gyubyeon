import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class ALUTest {

    @Test
    void enableSignal() {
        ALU alu = new ALU();
        alu.setOperand1(10);
        alu.setOperand2(20);
        alu.setOPCODE("ADD");

        Result ret = new Result();
        alu.enableSignal(ret);

        assertEquals(30, ret.getResult());
        assertEquals(0, ret.getStatus());
    }
}
