# unregisterWatermarkCallback

## 导入模块

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## unregisterWatermarkCallback

```TypeScript
function unregisterWatermarkCallback(callback?: WatermarkCallback): void
```

注销强制水印处理的监听事件。

**起始版本：** 24

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_PRINT

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [WatermarkCallback](arkts-basicservices-print-watermarkcallback-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
