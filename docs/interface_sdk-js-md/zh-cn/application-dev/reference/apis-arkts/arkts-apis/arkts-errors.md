# Errors(Defines the commonly used Errors for ArkTS)

Copyright (c) 2021-2026 Huawei Device Co., Ltd.
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 /


## 导入模块

```TypeScript
```

## 汇总

### 类

| 名称 | 说明 |
| --- | --- |
| [AggregateError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-aggregateerror-c.md) | AggregateError对象表示需要将多个错误包装为 单个错误时的错误。 |
| [ArgumentsUnderapplicationError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-argumentsunderapplicationerror-c.md) | 表示以错误方式对Function进行unsafe调用时抛出的错误。 |
| [ArithmeticError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-arithmeticerror-c.md) | 表示发生非法算术运算（例如除零）时抛出的错误。 |
| [ArrayIndexOutOfBoundsError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-arrayindexoutofboundserror-c.md) | 表示数组索引越界时发生的错误。 |
| [ArrayStoreError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-arraystoreerror-c.md) | 表示尝试将不同类型的对象存入类型擦除对象数组时抛出的错误。 |
| [AssertionError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-assertionerror-c.md) | 表示断言失败时发生的错误。 |
| [ClassCastError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-classcasterror-c.md) | 表示发生非法类型转换时抛出的错误。 |
| [CoroutinesLimitExceedError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-coroutineslimitexceederror-c.md) | 表示协程数量达到上限时抛出的错误。 |
| [DivideByZeroError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-dividebyzeroerror-c.md) | 表示执行除零运算时发生的错误。 |
| [EvalError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-evalerror-c.md) | 表示求值错误。 |
| [ExceptionInInitializerError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-exceptionininitializererror-c.md) | 表示初始化器中发生错误时抛出的错误。 |
| [FormatError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-formaterror-c.md) | 表示输入字符串包含非法数据或格式错误的数据时发生的错误。 |
| [IllegalLockStateError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-illegallockstateerror-c.md) | 表示锁处于非法状态时抛出的错误。 |
| [IllegalMonitorStateError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-illegalmonitorstateerror-c.md) | 表示对未同步的对象调用wait、notify或notifyAll时 抛出的错误。 |
| [IndexOutOfBoundsError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-indexoutofboundserror-c.md) | 表示传入的集合索引越界时抛出的错误。 |
| [InstantiationError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-instantiationerror-c.md) | 表示尝试实例化抽象类或接口时发生的错误。 |
| [InternalError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-internalerror-c.md) | 表示发生内部错误时的错误。 |
| [InvalidJobOperationError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-invalidjoboperationerror-c.md) | 表示对协程执行非法操作时抛出的错误。 |
| [InvalidStoreAccessError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-invalidstoreaccesserror-c.md) | 表示发生存储访问错误时抛出的错误。 |
| [JSONTypeError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-jsontypeerror-c.md) | 表示JSONValue无法赋值给某一类型时发生的错误。 |
| [NegativeArraySizeError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-negativearraysizeerror-c.md) | 表示传入负数数组长度时抛出的错误。 |
| [NonIntegralIndexError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-nonintegralindexerror-c.md) | 表示对索引表达式执行数值类型转换且小数部分不为0时 发生的错误。 |
| [NullPointerError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-nullpointererror-c.md) | 表示对空指针解引用时发生的错误。 |
| [OutOfMemoryError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-outofmemoryerror-c.md) | 表示内存分配失败时发生的错误。 |
| [RangeError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-rangeerror-c.md) | 表示传入的集合索引超出范围时发生的错误。 |
| [ReferenceError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-referenceerror-c.md) | 表示在当前作用域中引用不存在（或尚未初始化）的变量时 发生的错误。 |
| [StackOverflowError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-stackoverflowerror-c.md) | 表示可用内存不足以创建活动栈帧时发生的错误。 |
| [StringIndexOutOfBoundsError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-stringindexoutofboundserror-c.md) | 表示传入的字符串索引越界时抛出的错误。 |
| [SyntaxError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-syntaxerror-c.md) | 表示解析语法非法的代码时发生的错误。 |
| [TypeError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-typeerror-c.md) | 表示操作无法执行时发生的错误，通常（但不限于）是因为 值的类型不符合预期。 |
| [URIError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-urierror-c.md) | 表示以错误方式使用全局URI处理函数时发生的错误。 |
| [UncaughtExceptionError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-uncaughtexceptionerror-c.md) | 表示异常被抛出但未被捕获时发生的错误。 |

