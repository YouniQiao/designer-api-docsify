# Job

Represents a handle to a task's result, used to await the completion of a task.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class Job<T>--><!--Device-unnamed-export class Job<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

## Await

```TypeScript
Await(): T
```

Waits for the completion of the job and returns the result.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Job-Await(): T--><!--Device-Job-Await(): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | The result of the task. |

