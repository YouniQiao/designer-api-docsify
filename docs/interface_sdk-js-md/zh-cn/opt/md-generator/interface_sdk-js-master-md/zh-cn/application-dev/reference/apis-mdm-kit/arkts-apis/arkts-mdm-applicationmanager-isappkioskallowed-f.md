# isAppKioskAllowed

## 导入模块

```TypeScript
```

## isAppKioskAllowed

```TypeScript
function isAppKioskAllowed(appIdentifier: string): boolean
```

查询某应用是否允许在Kiosk模式下运行。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-applicationManager-function isAppKioskAllowed(appIdentifier: string): boolean--><!--Device-applicationManager-function isAppKioskAllowed(appIdentifier: string): boolean-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| appIdentifier | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
import { applicationManager } from '@kit.MDMKit';

try {
  // 需根据实际情况进行替换
  let isAllowed: boolean = applicationManager.isAppKioskAllowed('6917****3569');
  console.info(`Succeeded in querying if the app is allowed kiosk, isAllowed: ${isAllowed}`);
} catch (err) {
  console.error(`Failed to query if the app is allowed kiosk. Code is ${err.code}, message is ${err.message}`);
}
```
