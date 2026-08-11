# RestrictedWorker（系统接口）

RestrictedWorker类继承[ThreadWorker](arkts-arkts-worker-threadworker-c.md)，具有ThreadWorker中所有的方法。RestrictedWorker主要用于提供受限的Worker线程运行环境，该线程运行环境中只允许导入Worker模块，不允许导入其他API。

**继承/实现关系：** RestrictedWorker extends [ThreadWorker](arkts-arkts-worker-threadworker-c.md)

**起始版本：** 11

<!--Device-worker-class RestrictedWorker extends ThreadWorker--><!--Device-worker-class RestrictedWorker extends ThreadWorker-End-->

**系统能力：** SystemCapability.Utils.Lang

**系统接口：** 此接口为系统接口。

## constructor

```TypeScript
constructor(scriptURL: string, options?: WorkerOptions)
```

RestrictedWorker构造函数。使用其他方法前，均需先构造RestrictedWorker实例。

**起始版本：** 11

<!--Device-RestrictedWorker-constructor(scriptURL: string, options?: WorkerOptions)--><!--Device-RestrictedWorker-constructor(scriptURL: string, options?: WorkerOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scriptURL | string | 是 |
| options | [WorkerOptions](arkts-arkts-worker-workeroptions-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [10200003](../errorcode-utils.md#10200003-worker初始化失败) |
| [10200007](../errorcode-utils.md#10200007-worker文件路径异常) |
