# TimeZoneCityItem（系统接口）

时区城市的组合信息。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { i18n } from '@kit.LocalizationKit';
```

## cityDisplayName

```TypeScript
cityDisplayName: string
```

城市ID在系统区域下显示的名称。

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

## cityId

```TypeScript
cityId: string
```

城市ID，例如Shanghai。

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

## latitude

```TypeScript
latitude: double
```

以十进制度数表示的时区城市纬度信息(°)。

**类型：** number

**起始版本：** 26.1.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

## longitude

```TypeScript
longitude: double
```

时区城市的经度信息，十进制度数(°)。

**类型：** number

**起始版本：** 26.1.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

## offset

```TypeScript
offset: int
```

时区ID的偏移量，单位为毫秒（ms）。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

## rawOffset

```TypeScript
rawOffset?: int
```

时区ID的固定偏移量，单位为毫秒（ms）。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

## zoneDisplayName

```TypeScript
zoneDisplayName: string
```

时区ID在系统区域下显示的名称。

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。

## zoneId

```TypeScript
zoneId: string
```

时区ID，例如Asia/Shanghai。

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Global.I18n

**系统接口：** 此接口为系统接口。
