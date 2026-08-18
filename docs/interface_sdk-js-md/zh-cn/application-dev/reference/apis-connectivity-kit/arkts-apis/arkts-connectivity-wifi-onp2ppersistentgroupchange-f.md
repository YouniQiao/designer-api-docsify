# on_p2pPersistentGroupChange

## 导入模块

```TypeScript
```

## on_p2pPersistentGroupChange

```TypeScript
function on(type: 'p2pPersistentGroupChange', callback: Callback<void>): void
```

订阅P2P持久群组改变事件。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** p2pPersistentGroupChange

**需要权限：** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function on(type: 'p2pPersistentGroupChange', callback: Callback<void>): void--><!--Device-wifi-function on(type: 'p2pPersistentGroupChange', callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'p2pPersistentGroupChange' | 是 | 事件名称。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 | 状态改变回调函数 |

