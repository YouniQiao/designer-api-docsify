# AVSessionDescriptor

The description of the session

**Since:** 23

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-avSession-interface AVSessionDescriptor--><!--Device-avSession-interface AVSessionDescriptor-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

## Modules to Import

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## elementName

```TypeScript
elementName: ElementName
```

The elementName of the ability that created this session. See {@link ElementName} in bundle/elementName.d.ts

**Type:** [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AVSessionDescriptor-elementName: ElementName--><!--Device-AVSessionDescriptor-elementName: ElementName-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

## isActive

```TypeScript
isActive: boolean
```

Session active state

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AVSessionDescriptor-isActive: boolean--><!--Device-AVSessionDescriptor-isActive: boolean-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

## isTopSession

```TypeScript
isTopSession: boolean
```

Is it the top priority session

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AVSessionDescriptor-isTopSession: boolean--><!--Device-AVSessionDescriptor-isTopSession: boolean-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

## outputDevice

```TypeScript
outputDevice: OutputDeviceInfo
```

The current output device information.It will be undefined if this is a local session.

**Type:** [OutputDeviceInfo](arkts-avsession-avsession-outputdeviceinfo-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AVSessionDescriptor-outputDevice: OutputDeviceInfo--><!--Device-AVSessionDescriptor-outputDevice: OutputDeviceInfo-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

## sessionId

```TypeScript
sessionId: string
```

Unique ID of the session

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AVSessionDescriptor-sessionId: string--><!--Device-AVSessionDescriptor-sessionId: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

## sessionTag

```TypeScript
sessionTag: string
```

The session tag set by the application

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AVSessionDescriptor-sessionTag: string--><!--Device-AVSessionDescriptor-sessionTag: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

## type

```TypeScript
type: AVSessionType
```

Session type, currently supports audio or video

**Type:** [AVSessionType](arkts-avsession-avsession-avsessiontype-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AVSessionDescriptor-type: AVSessionType--><!--Device-AVSessionDescriptor-type: AVSessionType-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

