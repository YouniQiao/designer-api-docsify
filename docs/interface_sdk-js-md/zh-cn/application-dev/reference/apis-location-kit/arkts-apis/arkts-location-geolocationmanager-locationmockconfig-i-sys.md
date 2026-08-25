# LocationMockConfig（系统接口）

位置模拟功能的配置参数，包含了模拟位置上报的时间间隔和模拟位置数组。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## locations

```TypeScript
locations: Array<Location>
```

表示模拟位置数组。

**类型：** Array&lt;Location&gt;

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## timeInterval

```TypeScript
timeInterval: int
```

表示模拟位置上报的时间间隔，单位是秒。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。
