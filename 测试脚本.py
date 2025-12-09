# 测试脚本：检查Python环境和题库导入

print("Python环境正常")

# 尝试导入题库
try:
    from 传播学概论题库 import questions
    print(f"成功导入题库，共{len(questions)}道题")
    print(f"第1题: {questions[0]['question']}")
    print(f"第1题答案: {questions[0]['answer']}")
    print("\n测试成功！")
except Exception as e:
    print(f"导入失败: {e}")
    import traceback
    traceback.print_exc()