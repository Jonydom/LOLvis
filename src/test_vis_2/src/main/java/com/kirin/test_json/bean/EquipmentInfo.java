package com.kirin.test_json.bean;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

/**
 * @author Xiyao Li
 * @date 2022/12/24 02:05
 */
@Data
@AllArgsConstructor
@NoArgsConstructor
public class EquipmentInfo {
    private List<String> equip;
    private List<String> imgSrc;
    private Double pickRate;
    private Double games;
    private Double winRate;
}
