# isAppKioskAllowed

## 导入模块

```TypeScript
import { applicationManager } from 'kits/@kit.MDMKit';
```

## isAppKioskAllowed

```TypeScript
function isAppKioskAllowed(appIdentifier: string): boolean
```

查询某应用是否允许在Kiosk模式下运行。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| appIdentifier | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
