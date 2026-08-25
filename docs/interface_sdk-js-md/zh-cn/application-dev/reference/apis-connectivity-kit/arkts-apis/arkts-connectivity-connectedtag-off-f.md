# off

## 导入模块

```TypeScript
import { connectedTag } from 'kits/@kit.ConnectivityKit';
```

## off("notify")

```TypeScript
function off(type: "notify", callback?:Callback<number>): void
```

取消NFC场强状态事件的注册。

**起始版本：** 8

**需要权限：** ohos.permission.NFC_TAG

**系统能力：** SystemCapability.Communication.ConnectedTag

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | "notify" | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 否 |
