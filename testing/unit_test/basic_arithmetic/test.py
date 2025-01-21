import unittest
from predefined_functions.basic_arithmetic.FloatInput import FloatInputNode
from predefined_functions.basic_arithmetic.operations import MathOperations


class TestBasicArithmetic(unittest.TestCase):
    def test_float_input(self):
        f_ipt_node = FloatInputNode()
        opt = f_ipt_node.execute(float(5))[0]
        self.assertIsInstance(opt, float)

    def test_basic_arithmetic(self):
        f_ipt_node = FloatInputNode()
        op1 = f_ipt_node.execute(float(10))[0]
        op2 = f_ipt_node.execute(float(10))[0]
        m_op = MathOperations()
        res_1 = m_op.execute(op1, op2, "+")[0]
        self.assertEqual(res_1, op1 + op2)
        res_2 = m_op.execute(op1, op2, "-")[0]
        self.assertEqual(res_2, op1 - op2)
        res_3 = m_op.execute(op1, op2, "*")[0]
        self.assertEqual(res_3, op1 * op2)
        res_4 = m_op.execute(op1, op2, "/")[0]
        self.assertEqual(res_4, op1 / op2)
        res_5 = m_op.execute(op1, op2, "//")[0]
        self.assertEqual(res_5, op1 // op2)
        res_6 = m_op.execute(op1, op2, "**")[0]
        self.assertEqual(res_6, op1**op2)
        res_7 = m_op.execute(op1, op2, "%")[0]
        self.assertEqual(res_7, op1 % op2)
