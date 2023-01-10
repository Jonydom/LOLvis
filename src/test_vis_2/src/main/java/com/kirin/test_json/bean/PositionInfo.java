package com.kirin.test_json.bean;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

/**
 * @author Xiyao Li
 * @date 2022/12/24 01:43
 */
@Data
@AllArgsConstructor
@NoArgsConstructor
public class PositionInfo {
    private Double winRate;
    private Double pickRate;
    private Double banRate;

    private List<RuneInfo> runes;

    private List<EquipmentInfo> equipments;

    private List<CounterInfo> counters;
}
