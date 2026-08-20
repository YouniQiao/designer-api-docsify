# Particle

Defines Particle Component.

## Particle

```TypeScript
Particle(particles: Particles<
      PARTICLE,
      COLOR_UPDATER,
      OPACITY_UPDATER,
      SCALE_UPDATER,
      ACC_SPEED_UPDATER,
      ACC_ANGLE_UPDATER,
      SPIN_UPDATER
    >)
```

create a particle array.

Anonymous Object Rectification.

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-ParticleInterface-<    PARTICLE extends ParticleType,    COLOR_UPDATER extends ParticleUpdater,    OPACITY_UPDATER extends ParticleUpdater,    SCALE_UPDATER extends ParticleUpdater,    ACC_SPEED_UPDATER extends ParticleUpdater,    ACC_ANGLE_UPDATER extends ParticleUpdater,    SPIN_UPDATER extends ParticleUpdater  >(particles: Particles<      PARTICLE,      COLOR_UPDATER,      OPACITY_UPDATER,      SCALE_UPDATER,      ACC_SPEED_UPDATER,      ACC_ANGLE_UPDATER,      SPIN_UPDATER    >): ParticleAttribute--><!--Device-ParticleInterface-<    PARTICLE extends ParticleType,    COLOR_UPDATER extends ParticleUpdater,    OPACITY_UPDATER extends ParticleUpdater,    SCALE_UPDATER extends ParticleUpdater,    ACC_SPEED_UPDATER extends ParticleUpdater,    ACC_ANGLE_UPDATER extends ParticleUpdater,    SPIN_UPDATER extends ParticleUpdater  >(particles: Particles<      PARTICLE,      COLOR_UPDATER,      OPACITY_UPDATER,      SCALE_UPDATER,      ACC_SPEED_UPDATER,      ACC_ANGLE_UPDATER,      SPIN_UPDATER    >): ParticleAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| particles | [Particles](arkts-arkui-particles-i.md)&lt;PARTICLE, COLOR_UPDATER, OPACITY_UPDATER, SCALE_UPDATER, ACC_SPEED_UPDATER, ACC_ANGLE_UPDATER, SPIN_UPDATER&gt; | 是 | Array of particles. |

## 汇总

### 接口

| 名称 | 说明 |
| --- | --- |

### 类型

| 名称 | 说明 |
| --- | --- |
| [PositionT](arkts-arkui-positiont-t.md) | Defines the PositionT type. |

### 枚举

| 名称 | 说明 |
| --- | --- |

