# DisPlayInfo

```TypeScript
interface DisPlayInfo
```

Enterprise display information. This interface is used to set or query the enterprise customized copywriting(enterprise name) displayed on the lock screen and home page.

**Since:** 26.1.0

<!--Device-deviceSettings-interface DisPlayInfo--><!--Device-deviceSettings-interface DisPlayInfo-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { deviceSettings } from '@kit.MDMKit';
```

## enterpriseName

```TypeScript
enterpriseName: string
```

Enterprise display information. The inner layer is the JSON text of the enterprise name configured by language.

**Type:** string

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-DisPlayInfo-enterpriseName: string--><!--Device-DisPlayInfo-enterpriseName: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager
