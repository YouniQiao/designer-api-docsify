# markModuleCollectable（系统接口）

## markModuleCollectable

```TypeScript
export declare function markModuleCollectable(namespace: Object): void
```

Mark moduleNamespace which loaded by dynamic-import is collectable.

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function markModuleCollectable(namespace: Object): void--><!--Device-unnamed-export declare function markModuleCollectable(namespace: Object): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| namespace | Object | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
