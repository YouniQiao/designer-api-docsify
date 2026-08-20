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


## Modules to Import

```TypeScript
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [AggregateError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-aggregateerror-c.md) | AggregateError object represents an error when several errors need to be wrapped in a single error. |
| [ArgumentsUnderapplicationError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-argumentsunderapplicationerror-c.md) | Represents the error that is thrown when there is a wrong unsafe call to Function |
| [ArithmeticError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-arithmeticerror-c.md) | Represents error that is thrown when illegal arithmetic operation has occurred (e.g. division by zero) |
| [ArrayIndexOutOfBoundsError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-arrayindexoutofboundserror-c.md) | Represents an error that occurs when array is oging to be indexed out of its bounds |
| [ArrayStoreError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-arraystoreerror-c.md) | Represents error that is thrown when attempting to store an object of different type in array of type-erased objects |
| [AssertionError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-assertionerror-c.md) | Represents an error that occurs when assertion fails. |
| [ClassCastError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-classcasterror-c.md) | Represents error that is thrown in case of illegal class casting |
| [CoroutinesLimitExceedError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-coroutineslimitexceederror-c.md) | Represents error that is thrown when coroutines limit is reached |
| [DivideByZeroError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-dividebyzeroerror-c.md) | Represents an error that occurs when division by zero is performed. |
| [EvalError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-evalerror-c.md) | Represents an evaluation error |
| [ExceptionInInitializerError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-exceptionininitializererror-c.md) | Represents error that is thrown when there is an error in initializer |
| [FormatError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-formaterror-c.md) | Represents an error that occurs when an input string contains invalid or incorrectly formatted data. |
| [IllegalLockStateError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-illegallockstateerror-c.md) | Represents error that is thrown when lock is in an illegal state |
| [IllegalMonitorStateError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-illegalmonitorstateerror-c.md) | Represents an error that is thrown when attempting to wait, notify or notifyAll on object, that hasn't been synchronised |
| [IndexOutOfBoundsError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-indexoutofboundserror-c.md) | Represents error that is thrown when provided collection index is out of bounds |
| [InstantiationError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-instantiationerror-c.md) | Represents an error that occurs when attempting to instantiate abstract class or an interface |
| [InternalError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-internalerror-c.md) | Represents an error that occurs when an internal error has occurred |
| [InvalidJobOperationError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-invalidjoboperationerror-c.md) | Represents the error that is thrown when invalid operation is called on coroutine |
| [InvalidStoreAccessError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-invalidstoreaccesserror-c.md) | Represents the error that is thrown when there is store access error |
| [JSONTypeError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-jsontypeerror-c.md) | Represents an error that occurs when JSONValue can not be assigned to a type |
| [NegativeArraySizeError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-negativearraysizeerror-c.md) | Represents error that is thrown when negative array size is supplied |
| [NonIntegralIndexError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-nonintegralindexerror-c.md) | Represents an error that occurs when a numeric types conversion is performed on an index expression, and the fractional part differs from 0. |
| [NullPointerError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-nullpointererror-c.md) | Represents an error that occurs when null pointer is dereferenced. |
| [OutOfMemoryError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-outofmemoryerror-c.md) | Represents an error that occurs when memory allocation fails |
| [RangeError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-rangeerror-c.md) | Represents an error that occurs when provided collection index is out of range |
| [ReferenceError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-referenceerror-c.md) | Represents an error that occurs when a variable that doesn't exist (or hasn't yet been initialized) in the current scope is referenced |
| [StackOverflowError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-stackoverflowerror-c.md) | Represents an error that occurs when the available memory is not sufficient to create the activation frame |
| [StringIndexOutOfBoundsError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-stringindexoutofboundserror-c.md) | Represents error that is thrown when provided string index is out of bounds |
| [SyntaxError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-syntaxerror-c.md) | Represents an error that occurs when trying to interpret syntactically invalid code |
| [TypeError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-typeerror-c.md) | Represents an error that occurs when an operation could not be performed, typically (but not exclusively) when a value is not of the expected type |
| [URIError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-urierror-c.md) | Represents an error that occurs when a global URI handling function was used in a wrong way |
| [UncaughtExceptionError(Defines the commonly used Errors for ArkTS)](arkts-arkts-errors-uncaughtexceptionerror-c.md) | Represents an error that occurs when exception is thrown and not caught |

