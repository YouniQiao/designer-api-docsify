# DisPlayInfo

```TypeScript
interface DisPlayInfo
```

企业展示信息。用于设置/查询锁屏与设置首页展示的企业定制文案（企业名称）。

**起始版本：** 26.1.0

<!--Device-deviceSettings-interface DisPlayInfo--><!--Device-deviceSettings-interface DisPlayInfo-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## 导入模块

```TypeScript
import { deviceSettings } from '@kit.MDMKit';
```

## enterpriseName

```TypeScript
enterpriseName: string
```

企业展示信息，内层为按语言分别配置企业名称的 JSON 文本。

**类型：** string

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DisPlayInfo-enterpriseName: string--><!--Device-DisPlayInfo-enterpriseName: string-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager
