# UidNetStatsInfo（系统接口）

```TypeScript
export type UidNetStatsInfo = {
    [uid: int]: NetStatsInfo;
  }
```

{@link NetStatsInfo} for every UID. Key is UID.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-statistics-export type UidNetStatsInfo = {    [uid: int]: NetStatsInfo;  }--><!--Device-statistics-export type UidNetStatsInfo = {    [uid: int]: NetStatsInfo;  }-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

**属性类型：** {
    [uid: int]: NetStatsInfo;
  }

