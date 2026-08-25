# finishTrace

## 导入模块

```TypeScript
```

## finishTrace

```TypeScript
function finishTrace(name: string, taskId: number): void
```

标记一个时间片跟踪事件的结束。

> **说明：**&gt;
> - finishTrace的name和taskId必须与流程开始的startTrace对应参数值一致。
> - 从API version 7开始支持，从API version 8开始废弃。

**起始版本：** 7

**废弃版本：** 8

**替代接口：** finishTrace

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| taskId | number | 是 |
