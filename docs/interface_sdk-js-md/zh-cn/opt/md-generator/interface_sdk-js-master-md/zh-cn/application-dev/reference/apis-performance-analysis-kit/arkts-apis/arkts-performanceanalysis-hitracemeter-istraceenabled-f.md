# isTraceEnabled

## 导入模块

```TypeScript
```

## isTraceEnabled

```TypeScript
function isTraceEnabled(): boolean
```

判断当前是否开启应用trace捕获。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-hiTraceMeter-function isTraceEnabled(): boolean--><!--Device-hiTraceMeter-function isTraceEnabled(): boolean-End-->

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
if (hiTraceMeter.isTraceEnabled()) {
  // 业务流程......
} else {
  // 业务流程......
}
```
