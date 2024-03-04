import matplotlib.pyplot as plt
import numpy as np


class RadarChart:
    def __init__(self, categories, levels, yticks_labels=None, area_color='red', line_style='dotted'):
        self.categories = categories
        self.levels = levels
        self.num_vars = len(categories)
        self.yticks_labels = yticks_labels or {}
        self.area_color = area_color
        self.line_style = line_style

    def _calculate_angles(self):
        """Calculate angles for radar chart categories."""
        return np.linspace(0, 2 * np.pi, self.num_vars, endpoint=False).tolist() + [0]

    def _setup_chart(self, ax):
        """Set up the radar chart, including axes and gridlines."""
        angles = self._calculate_angles()
        ax.set_theta_offset(np.pi / 2)
        ax.set_theta_direction(-1)

        # Draw axes labels
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(self.categories, size=10, color='black', fontweight='roman')

        # Configure y-ticks
        yticks = np.arange(1, 7)
        yticklabels = [self.yticks_labels.get(ytick, '') for ytick in yticks]
        ax.set_yticks(yticks)
        ax.set_yticklabels(yticklabels)
        ax.set_ylim(0, 6)
        # Add custom y-tick labels if provided
        if self.yticks_labels:
            for cat, angle in zip(self.categories, angles):
                if cat in self.yticks_labels:
                    for level, label in enumerate(self.yticks_labels[cat], start=1):
                        ax.text(angle,
                                level,
                                label,
                                horizontalalignment='left',
                                verticalalignment='top',
                                size=8,
                                color='grey',
                                fontweight='roman',
                                )

        # Remove the default grid and outer circle
        ax.yaxis.grid(False)
        ax.spines['polar'].set_visible(False)

        # Custom dotted lines
        for ytick in yticks:
            ax.plot(angles, [ytick] * len(angles), linestyle=(0, (6, 6)), color="grey", linewidth=0.4)
        ax.plot(angles, [yticks[-1]] * len(angles), linestyle=(0, (1, 0)), color="black", linewidth=0.6)

    def _plot_data(self, ax, angles):
        """Plot the data on the radar chart."""
        values = [self.levels[cat] for cat in self.categories] + [self.levels[self.categories[0]]]
        ax.plot(angles, values, linewidth=2, linestyle='solid', color=self.area_color)
        ax.fill(angles, values, color=self.area_color, alpha=0.1)

    def create_chart(self, output_filename):
        fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
        self._setup_chart(ax)
        angles = self._calculate_angles()
        self._plot_data(ax, angles)

        # Add bot at the center
        ax.plot(0, 0, 'o', markersize=10, color='royalblue')
        ax.plot(0, 0, 'o', markersize=3, color='white')

        plt.savefig(output_filename, bbox_inches='tight')
        plt.close()


# Example usage:
categories = ['Technology', 'System', 'People', 'Process', 'Influence']

# Define custom y-tick labels for each category
yticks_labels = {
    'Technology': ["Adopts", "Specializes", "Evangelizes", "Masters", "Creates"],
    'System': ["Enhances", "Designs", "Owns", "Evolves", "Leads"],
    'People': ["Learns", "Supports", "Mentors", "Coordinates", "Manages"],
    'Process': ["Follows", "Enforces", "Challenges", "Adjusts", "Defines"],
    'Influence': ["Individual", "Team", "Platform", "Engineering", "Company"],
}


axes_desc = """
## Axes - 위 차트에 속한 5가지의 축

### Technology: 기술 스택 및 도구에 대한 지식

* 데이터 과학 도구 및 기술에 대한 지식: 데이터 수집, 처리, 분석, 시각화 및 모델링을 위한 다양한 도구와 프로그래밍 언어(Python, R 등)에 대한 깊은 이해가 필요합니다. 또한, 머신러닝 라이브러리와 프레임워크(TensorFlow, PyTorch, scikit-learn 등) 사용 능력을 키워야 합니다.

### System: 시스템의 소유권 수준

* 데이터 처리 시스템과 모델링 접근 방식의 소유권 수준: 데이터 파이프라인 구축 및 최적화, 대규모 데이터셋 관리, 클라우드 서비스(AWS, Google Cloud, Azure 등) 활용 능력, 데이터 거버넌스 및 보안에 대한 이해가 중요합니다.

### People: 팀과의 관계

* 팀과의 협업: 다른 데이터 사이언티스트, 데이터 엔지니어, 제품 관리자 등과의 효과적인 커뮤니케이션과 협업 능력이 필요합니다. 이해관계자의 요구사항을 정확히 파악하고, 결과를 명확하게 전달할 수 있어야 합니다.

### Process: 개발 프로세스에 대한 참여 수준

* 데이터 과학 프로젝트 수행 방법에 대한 참여 수준: 데이터 과학 프로젝트의 생명주기(문제 정의, 데이터 수집, 데이터 정제, 탐색적 데이터 분석, 모델링, 평가, 배포)를 이해하고, Agile, SCRUM 등의 개발 방법론을 데이터 과학 프로젝트에 적용할 수 있어야 합니다.

### Influence: 역할의 영향 범위

* 역할의 영향 범위: 개인, 팀, 조직 내외부에 미치는 영향력을 확장하는 능력입니다. 데이터 기반 의사 결정 촉진, 데이터 문화 형성 기여, 데이터와 관련된 최신 동향과 기술을 팀이나 조직에 전파하고, 데이터 사이언스를 통해 비즈니스 및 기술 혁신을 주도하는 능력이 포함됩니다.
"""


datascience_desc = {
    'Technology': {
        1: """
#### Adopts: 팀이 정의한 데이터 과학 기술과 도구를 적극적으로 배우고 적용합니다

* 데이터 처리 및 분석 방법론 이해: 팀이 정한 데이터 사이언스 관련 컨벤션, 분석 방법론, 정책들을 이해하고, 데이터의 정확성, 가독성, 재사용성을 고려하여 분석 과정을 설계합니다.

* 데이터 검증을 위한 테스트 구현: 데이터 분석의 정확성을 보장하기 위해 적절한 데이터 검증 절차를 마련하고, 테스트 케이스를 도출하여 데이터의 품질을 검증합니다.

* 독립적 문제 해결 능력: 데이터 분석 및 모델링 과정에서 발생하는 다양한 문제를 독립적으로 해결할 수 있는 능력을 개발하고, 필요한 데이터 사이언스 기술과 도구를 적용하여 복잡한 분석 문제를 해결합니다.
        """,
        2: """
#### Specializes: 특정 데이터 과학 분야에 전문성을 가지며 새로운 기술을 주도적으로 학습합니다

* 전문 분야의 깊은 이해: 하나 이상의 데이터 과학 분야(예: 머신러닝, 딥러닝, 통계 분석, 자연어 처리 등)에서 깊은 전문 지식을 보유하고, 해당 분야의 최신 연구와 발전을 지속적으로 학습합니다.

* 업계 동향과 데이터 인프라에 대한 폭넓은 지식: 데이터 과학과 관련된 최신 업계 동향, 표준, 사내 데이터 처리 및 분석 인프라에 대한 광범위한 이해를 바탕으로, 조직의 데이터 과학 전략과 프로젝트에 기여합니다.

* 데이터 분석 및 모델링의 모범 사례: 데이터 분석 및 모델링 과정에서 고품질의 결과물을 생산하기 위해 모범 사례와 최적의 접근 방식을 적용하고, 이를 팀 내외의 동료들과 공유합니다.

* 복잡한 데이터 프로젝트의 관리: 증가하는 복잡성을 가진 데이터 프로젝트를 end-to-end로 이해하고 관리할 수 있는 능력을 발휘하며, 프로젝트의 성공을 위해 필요한 분석, 모델링, 데이터 처리 코드에 기여합니다.

* 의사 결정과 설계 절충안: 데이터 과학 프로젝트와 관련된 의사 결정 과정에서 발생할 수 있는 다양한 설계 절충안을 이해하고, 합리적인 결정을 내립니다.

* 기술적 조언과 리더십: 동료들에게 데이터 과학 분야에서 발생하는 기술적 문제에 대한 조언과 가이드를 제공하며, 팀 내 데이터 과학 역량 강화를 위한 리더십을 발휘합니다.

* 기술 부채의 관리: 데이터 과학 프로젝트 수행 과정에서 발생할 수 있는 기술 부채를 조기에 식별하고, 이를 관리하거나 해결하는 전략을 세우고 실행합니다.
        """,
        3: """
#### Evangelizes: 데이터 과학 분야에서의 연구 조사와 개념 증명(POC)을 통해 새로운 기술을 팀에 소개합니다

* 새로운 데이터 과학 기술의 도입: 최신 데이터 과학 연구와 기술 동향을 탐색하고, 이를 기반으로 실질적인 개념 증명(POC) 프로젝트를 수행하여 팀 내에 새로운 접근 방식이나 도구를 소개합니다. 이 과정에서 데이터 과학 프로젝트의 효율성과 정확성을 향상시킬 수 있는 혁신적인 방법을 탐구합니다.

* 데이터 인프라와 분석 시스템의 전문가: 데이터 처리 및 분석 인프라, 데이터 파이프라인, 머신러닝 모델링 플랫폼 등 데이터 과학 기술 스택의 핵심 부분에서 발생하는 복잡한 문제를 해결하는 데 기여합니다. 조직 전체에 걸친 데이터 인프라의 최적화와 개선 작업을 주도하여 데이터 과학 팀의 생산성을 증가시킵니다.

* 아키텍처 및 시스템 설계의 리더십: 데이터 과학 프로젝트의 광범위한 아키텍처를 설계하고, 대규모 데이터 처리 시스템, 복잡한 분석 모델, 핵심 데이터 저장소 등의 기술적 방향을 제시합니다. 이를 통해 조직의 데이터 처리, 분석, 모델링 능력을 향상시키며, 주요 데이터 서비스의 안정성, 성능, 확장성을 개선합니다.

* 기술적 문제의 식별 및 해결: 데이터 과학 프로젝트와 시스템 전반에 걸친 설계와 구현에서 발생할 수 있는 문제점을 식별하고, 이를 해결하기 위한 전략을 개발합니다. 복잡한 데이터 과학 문제를 해결하는 데 필요한 조정과 협업을 주도하여, 프로젝트의 성공적인 수행을 보장합니다.

* 내부 교육과 지식 공유: 데이터 과학 팀 내외에서 지속적인 학습과 지식 공유의 문화를 조성하고, 워크숍이나 세미나를 통해 팀원들의 기술 역량을 강화합니다. 이러한 활동을 통해 팀 내의 기술적 리더십을 발휘하며, 데이터 과학 분야에서의 혁신을 촉진합니다.
        """,
        4: """
#### Masters: 데이터 과학의 전체 기술 스택에 대해 매우 깊은 지식을 가지고 있습니다

* 데이터 과학 분야의 권위자: 데이터 수집, 처리, 분석, 시각화 및 모델링에 이르기까지 데이터 과학의 전체 기술 스택에 대한 깊은 이해를 바탕으로, 조직 내외부에서 기술적 리더십과 멘토십을 발휘합니다.

* 롤모델과 멘토: 데이터 과학 커뮤니티 내에서 신뢰받는 롤모델이자 멘토로 활동하며, 지식과 경험을 공유하여 팀원과 조직의 데이터 과학 역량을 강화합니다.

* 아키텍처와 비즈니스 이해: 조직의 데이터 아키텍처와 관련된 비즈니스 요구사항을 깊이 이해하고, 데이터 과학 솔루션이 비즈니스 목표를 달성하는 데 어떻게 기여할 수 있는지 명확하게 설명할 수 있습니다. 데이터 솔루션의 확장성과 신뢰성에 대한 한계와 가능성을 정확히 평가합니다.

* 혁신과 기술 도입: 최신 데이터 과학 연구와 기술을 지속적으로 탐구하고, 새로운 기술이나 방법론을 조직 내에 도입하여 데이터 과학 프로젝트의 성공을 이끕니다. 내부 및 외부 팀과 협력하여 혁신적인 데이터 과학 솔루션을 개발하고 구현합니다.

* 기술적 성장의 주도: 조직의 데이터 과학 전략과 기술 로드맵을 개발하고 실행하며, 데이터 과학 분야에서의 기술 혁신을 주도합니다. 데이터 과학 팀과 조직 전체의 기술적 성장과 발전에 결정적인 기여를 하며, 데이터 기반 의사 결정 문화를 촉진합니다.
        """,
        5: """
#### Creates: 데이터 과학 분야에서 조직 내외부 팀이 널리 사용할 혁신적인 솔루션을 디자인하고 개발합니다

* 혁신적 솔루션의 개발: 새로운 데이터 과학 기술, 알고리즘, 도구를 개발하여 데이터 분석 및 모델링 작업의 효율성과 효과성을 극대화합니다. 이러한 혁신은 내부 팀 뿐만 아니라 업계 전반에 영향을 미칠 수 있습니다.

* 데이터 과학 전략의 방향성 설정: 데이터 과학 기술의 발전 방향을 설정하고, 조직의 데이터 분석 및 모델링 능력을 향상시키는 데 중요한 기술적 결정을 내립니다. 장기적인 성공을 위한 전략적 비전을 제공합니다.

* 다년간의 기술 전략 개발: 조직의 비즈니스 목표와 밀접하게 연결된 데이터 과학 기술 전략을 수립합니다. 이 전략은 여러 시스템, 팀, 플랫폼을 아우르는 비즈니스의 핵심 영역에 대한 깊은 이해를 바탕으로 합니다.

* 기술 변화에 대한 선제적 대응: 데이터 과학 분야에서 발생하는 광범위한 기술 변화를 예측하고, 최신 기술 트렌드를 지속적으로 모니터링합니다. 이를 바탕으로 조직이 빠르게 변화하는 데이터 과학 환경에서 경쟁력을 유지할 수 있도록 전략을 수립하고 실행합니다.

* 기술 역량 강화 및 표준화: 조직 내 데이터 과학 역량을 강화하기 위한 다양한 활동(워크숍, 세미나, 이니셔티브, 코드 리뷰 등)을 주도합니다. 이를 통해 팀원들 사이의 기술적 격차를 최소화하고, 조직 전체의 데이터 과학 수준을 높입니다.

* 채용 과정에서의 기술적 리더십: 채용 과정에 적극적으로 참여하여, 후보자가 조직의 데이터 과학 기술 표준과 문화에 부합하는지 평가합니다. 이를 통해 조직이 우수한 데이터 과학 인재를 확보하고 유지할 수 있도록 합니다.

""",
    },
    'System': {
        1: """
#### Enhances: 데이터 시스템의 개선 및 확장을 위해 새로운 분석 기능을 개발하고 데이터 관련 문제를 해결합니다

* 데이터 요구사항 분석과 설계: 복잡한 데이터 분석 요구사항을 체계적으로 분석하고, 이를 구현하기 위한 데이터 모델, 알고리즘, 처리 과정 등의 구성 요소를 식별합니다. 이를 관리 가능하고 실행 가능한 작은 단위로 분해하여, 효율적으로 문제를 해결할 수 있는 계획을 수립합니다.

* 작업 우선순위 결정: 프로젝트의 전체 목표와 긴급도를 고려하여, 중요한 작업과 긴급한 버그 수정에 우선순위를 두고 작업합니다. 이를 통해 리소스를 효과적으로 할당하고, 프로젝트 진행에 있어 중요한 세부사항에 집중할 수 있습니다.

* 협업과 지원 요청: 데이터 분석 및 모델링 과정에서 발생할 수 있는 병목 현상이나 기술적 난제를 조기에 식별하고, 필요한 경우 동료나 관리자에게 적절한 시기에 도움을 요청함으로써 작업의 연속성과 프로젝트의 성공적인 완료를 보장합니다.

* 지속적인 학습과 적용: 데이터 과학 및 분석 분야의 최신 기술, 도구, 방법론을 지속적으로 학습하고, 이를 실제 프로젝트에 적용하여 데이터 시스템의 성능을 개선하고, 분석 결과의 정확성을 높입니다. 조직 내 다른 팀과의 협업을 통해 얻은 경험과 지식을 바탕으로, 데이터 처리와 분석 프로세스를 지속적으로 최적화합니다.
""",
        2: """
#### Designs: 중대형 데이터 과학 프로젝트를 기술 부채를 관리하며 설계 및 구현합니다

* 복잡한 데이터 요구사항의 해석과 구현: 중대형 데이터 과학 프로젝트의 복잡한 요구사항을 정확히 이해하고, 이를 충족시키는 데이터 모델, 알고리즘, 분석 방법론을 설계합니다. 이 과정에서 데이터의 품질과 분석의 정확성을 최우선으로 고려하여 오류를 최소화합니다.

* 프로젝트 관리 및 단계적 실행: 프로젝트의 범위를 명확히 정의하고, 잘 계획된 마일스톤에 따라 작업을 조직합니다. 이를 통해 단계적으로 프로젝트를 실행하며, 각 단계에서의 결과물을 지속적으로 검토하고 조정합니다.

* 문제 식별 및 조기 해결: 프로젝트 진행 중 발생할 수 있는 다양한 문제(명확하지 않은 요구사항, 요구사항 간의 불일치, 기술적 제한 등)를 조기에 식별하고, 이에 대한 해결책을 모색합니다. 이를 통해 프로젝트의 방향을 적절히 조정하고, 팀원들과의 커뮤니케이션을 강화합니다.

* 기술 부채의 관리: 새로운 기능을 추가하면서 동시에 기존의 기술 부채를 식별하고 줄여나가는 전략을 수립합니다. 이를 통해 장기적인 프로젝트의 유지보수성과 확장성을 보장합니다.

* 사용자 중심의 설계: 최종 사용자의 필요와 불편 사항을 깊이 이해하고, 이를 프로젝트 설계에 반영하여 사용자 친화적인 데이터 과학 솔루션을 개발합니다. 사용자의 피드백을 적극적으로 수집하고 분석하여 의사 결정 과정에 반영합니다.

* 효과적인 문제 해결: 할당된 문제를 넘어 프로젝트 전반에서 발생할 수 있는 잠재적 장애를 사전에 파악하고, 이를 해결하기 위한 효과적인 접근 방식을 개발합니다. 이 과정에서 데이터 과학 팀의 역량을 최대한 활용하여 프로젝트의 성공을 이끕니다.
""",
        3: """
#### Owns: 데이터 과학 프로젝트의 운영 및 모니터링에 대한 책임을 지며, 서비스 수준 협약(SLAs)을 준수합니다

* 데이터 시스템의 운영 책임: 데이터 분석 및 모델링 프로젝트의 프로덕션 환경에서의 운영과 모니터링을 책임지며, 정의된 서비스 수준 협약(SLAs)을 충족시키기 위한 전략과 계획을 수립합니다.

* 기술적 우수성의 확보: 데이터 과학 시스템의 기술적 품질과 성능을 지속적으로 관리하고 개선하여, 시스템의 우수성을 유지합니다. 이를 위해 최신 데이터 과학 기술과 방법론을 적극적으로 도입하고 적용합니다.

* 복잡한 문제 해결 리더십: 프로젝트나 서비스에서 발생할 수 있는 복잡하고 정의되지 않은 문제를 주도적으로 해결합니다. 문제 해결 과정에서 팀원들을 조율하고, 효과적인 솔루션을 설계 및 구현합니다.

* 출시 계획과 공수 산정: 비즈니스 요구사항과 일정에 따라 데이터 과학 프로젝트의 출시 계획을 수립하고, 필요한 리소스와 공수를 정확히 산정합니다. 이를 바탕으로 프로젝트 일정을 관리하고, 이해관계자에게 명확하게 소통합니다.

* 요구사항 간의 균형 이해: 기술적, 분석적, 시스템적 요구사항 사이의 균형을 완벽하게 이해하고, 이를 바탕으로 상황에 적합한 데이터 솔루션을 선택 및 적용합니다. 이 과정에서 다양한 이해관계자의 요구와 기대를 조율합니다.

* 프로젝트 복잡성 관리: 데이터 과학 프로젝트와 서비스의 복잡성을 지속적으로 평가하고, 이를 최소화하기 위한 방안을 실행합니다. 이를 통해 더 효율적이고 효과적인 작업 수행을 가능하게 합니다.

* 다부서 협업: 제품, 비즈니스 개발, 디자인 등 조직 내 다른 부서와 긴밀히 협력하여, 모든 당사자의 요구사항을 반영한 최적의 데이터 과학 솔루션을 설계하고 구현합니다. 이를 통해 조직의 데이터 기반 의사 결정과 혁신을 촉진합니다.
""",
        4: """
#### Evolves: 미래의 데이터 과학 요구사항을 지원하기 위한 설계 발전 및 서비스 수준 협약(SLAs) 정의

* 미래 지향적 설계 개발: 데이터 과학 프로젝트와 시스템을 설계할 때, 미래의 데이터 분석 요구와 확장성을 고려하여 유연하고 확장 가능한 아키텍처를 개발합니다. 이를 통해 장기적인 비즈니스 목표와 데이터 과학 요구사항을 충족시키는 설계 방향을 제시합니다.

* 서비스 수준 협약(SLAs)의 정립: 데이터 과학 서비스의 품질과 성능을 보장하기 위해 명확한 서비스 수준 협약(SLAs)을 정의하고, 이를 기반으로 데이터 분석 및 모델링 프로세스의 운영 표준을 설정합니다. 이 SLAs는 데이터 처리 속도, 모델 정확도, 시스템 가용성 등을 포함할 수 있습니다.

* 문제 해결의 체계화: 데이터 과학 프로젝트에서 발생할 수 있는 다양한 문제를 식별하고, 이를 구조화된 방법으로 분류하여 체계적인 문제 해결 접근 방식을 개발합니다. 이를 통해 문제 해결의 효율성을 높이고, 프로젝트의 성공 가능성을 증대시킵니다.

* 효과적인 작업 관리 및 우선순위 설정: 다수의 작업 트랙과 프로젝트를 동시에 관리하면서, 가장 중요하고 긴급한 작업에 우선순위를 부여합니다. 이를 통해 리소스를 최적화하고, 프로젝트 목표 달성에 필요한 핵심 작업에 집중할 수 있습니다.

* 기술 아키텍처의 지속적 개선: 데이터 과학 시스템의 기술 아키텍처를 지속적으로 검토하고 개선하여, 향후 비즈니스와 데이터 과학의 변화하는 요구사항을 효과적으로 지원할 수 있는 구조를 마련합니다. 이를 위해 최신 데이터 과학 기술과 트렌드를 적극적으로 탐색하고 적용합니다.

* 복잡한 문제의 전략적 해결: 조직 전체에 영향을 미치는 크고 모호한 문제를 인식하고, 이를 해결하기 위해 다학제 팀을 조직하고 리드합니다. 문제 해결 과정에서 데이터 과학의 깊은 전문 지식과 비즈니스 이해를 바탕으로 효과적인 해결책을 도출합니다.
        """,
        5: """
#### Leads: 데이터 과학 시스템의 기술적 우수성을 리드하고 시스템의 안정성을 최대화하기 위한 계획을 수립합니다

* 기술적 리더십의 발휘: 데이터 과학 분야에서 기술적 우수성을 추구하며, 데이터 분석 및 모델링 시스템의 안정성과 효율성을 지속적으로 개선합니다. 최신 데이터 과학 기술을 적극적으로 도입하여 시스템의 혁신을 주도합니다.

* 팀 간 협업 촉진: 다양한 팀과 플랫폼 간의 협업을 촉진하여, 조직 전체의 데이터 과학 목표 달성을 지원합니다. 이를 통해 비즈니스 및 엔지니어링 목표에 중대한 영향을 미치며, 조직 내 데이터 기반 문화를 강화합니다.

* 비즈니스 성장을 위한 기술 전략 개발: 비즈니스 목표와 연계된 데이터 과학 전략을 수립하고, 조직의 성장에 기여할 수 있는 새로운 기술적 기회를 식별합니다. 데이터 과학을 통해 비즈니스 가치를 극대화할 수 있는 방안을 모색합니다.

* 핵심 영역의 개선 계획 수립: 조직 내 데이터 과학 시스템에서 가장 중요한 영역을 파악하고, 이를 개선하기 위한 전략적 계획을 수립합니다. 이를 통해 데이터 처리, 분석 및 모델링의 효율성과 정확성을 높입니다.

* 시스템적 문제 예방: 데이터 과학 시스템 전반에 걸친 기술적 문제를 사전에 예측하고, 이를 방지하기 위한 아키텍처 및 디자인 결정을 내립니다. 잠재적인 문제를 미리 식별하고 해결함으로써 시스템의 안정성과 지속 가능성을 보장합니다.
""",
    },

    'People': {
        1: """
#### Learns: 다른 사람들로부터 빠르게 학습하고 그것들을 필요로 하는 업무들을 지속적으로 수행해 나갑니다

* 협력적인고 도움이 되고, 호기심 많은 팀원입니다.

* 작업 상태를 팀에 효과적으로 전달할 수 있습니다.

* 재 작업을 최소화하기 위해 작업에 대한 이해의 수준을 팀과 동기화 합니다.

* 어떤 문제에 대해 자신의 의견을 명확하게 전달하고 적절한 해결책을 찾는 노력을 합니다.
""",
        2: """
#### Supports: 다른 팀원들을 적극적으로 지원하고 성공할 수 있도록 돕습니다

* 자신의 의견에 대해 문서와 대화를 통해 기술적 결정을 명확하게 전달합니다.

* 다양한 영역에 코드리뷰에 참여하고 코드리뷰, 페어프로그래밍을 통해 다른 동료를 돕습니다.

* 다른 팀간의 효과적인 커뮤니케이션이 가능하고 다양한 팀 (Product, BD, Design)과 원할하게 협력할 수 있습니다.

* 피드백을 건설적인 방식으로 처리하며 피드백으로부터 배우기 위해 최선을 다합니다.

* 복잡한 문제와 대규모 작업을 조직 내부의 다양한 청중에게 이해하기 쉽고 편안하게 전달합니다.""",
        3: """
#### Mentors: 다른 사람들을 멘토링하여 경력 성장을 가속화하고 참여를 독려합니다

* 팀에서 수행되는 엔지니어링의 전반적인 품질을 향상시키고 팀원의 성공을 지원하기 위한 조치를 지속적으로 취합니다.

* 팀 간 작업을 아르고의 비즈니스 및 엔지니어링 우선순위에 맞춰 조정하여 의미있는 영향을 실현합니다.

* 합의에 도달하는데 도움이 되도록 토론을 듣고 안내합니다. 결정이 내려지면 명확하게 전달하고 해당 결정을 지지합니다.

* 동료와 관리자에게 시기적절하고 유용한 피드백을 제공합니다.

* 사람들과 관련된 소모임에 실질적인 기여를 합니다.""",

        4: """
#### Coordinates: 효과적인 피드백을 제공하고 토론을 주도합니다

* 팀의 모든 기술 구성원의 롤모델이자 멘토로 간주됩니다.

* 복잡한 프로젝트에서 팀을 조정하고 실행을 계획하며 영향력과 생산성을 높이는데 역할을 합니다.

* 팀과 관련된 회의, 토론을 진행하고 조치해야되는 내용을 수집하여 이에 대한 추적/후속 조치를 취합니다.

* 팀에 영향을 미치는 기술 문제에 대한 전략을 식별 및 제안하고, 표준을 전달하여 솔루션에 대한 동의를 이끌어냅니다.

* 공식적으로든 비공식적으로든 개인에 맞게 멘토링 할 수 있고 올바른 경험과 지식을 공유합니다.""",
        5: """
#### Manages: 팀원들의 커리어, 기대 수준, 성과, 행복 수준를 관리합니다

* 아르고 전방에 걸쳐 엔지니어와 비엔지니어 모든 팀/팀원의 고른 성장과 성공을 지원하기 위한 조치를 지속적으로 취하고 있습니다.

* 효과적인 피드백을 제공하고 팀원의 성과, 기대치, 행복 수준을 관리합니다.

* 각 팀 구성원에게 개인적인 6~12개월 성장 전략을 명확하게 전달하고 충실히 수행되고 있는지 추적/반복적인 피드백을 전달하여 팀 구성원들의 성장을 이끌어 냅니다.

* 팀의 크고 작은 성공과 개발 팀원의 성취를 위한 동기를 부여할 수 있습니다.

* 채용 과정에서 핵심적인 역할을 수행하여 후보자가 우리 엔지니어링 조직에 적합한지 확인합니다.""",
    },

    'Process': {
        1: """
#### Follows: 팀 프로세스를 준수하며 데이터 과학 프로젝트에 일관된 결과물을 제공합니다

* 데이터 과학 프로젝트의 워크플로와 팀 내 프로세스를 정확히 이해하고, 이를 철저하게 실행합니다. 이를 통해 데이터 분석 및 모델링 작업의 일관성과 품질을 보장합니다.

""",
        2: """
#### Enforces: 팀 프로세스를 강화하며 모든 구성원이 이의 가치를 이해하게 합니다

* 프로젝트 진행 중 발견된 프로세스의 문제점을 식별하고, 이에 대한 개선안을 제안하여 팀의 효율성과 생산성을 증가시킵니다. 모든 팀원이 프로세스의 중요성을 인식하고 이를 준수하도록 합니다.""",
        3: """
#### Challenges: 기존 프로세스에 도전하며 개선점을 찾아 적용합니다

* 데이터 과학 프로젝트의 특성에 맞게 기존 프로세스를 재검토하고, 더 효율적인 방식을 모색합니다. 이를 통해 불필요한 작업을 줄이고, 더 나은 결과물을 신속하게 도출할 수 있습니다.""",
        4: """
#### Adjusts: 피드백을 기반으로 프로세스를 조정하고 팀을 이끕니다

* 프로젝트 진행 중 수집된 피드백을 바탕으로 프로세스를 지속적으로 조정하며, 이러한 변경사항을 팀에 명확히 전달합니다. 내부 워크숍이나 회의를 통해 프로세스 개선을 위한 논의를 촉진하고, 구성원들의 참여를 독려합니다.""",
        5: """
#### Defines: 데이터 과학 팀의 성장 단계에 맞는 적절한 프로세스를 정립합니다

* 데이터 과학 분야의 독특한 요구사항과 팀의 성숙도를 고려하여, 민첩하면서도 체계적인 개발 및 분석 워크플로를 설계합니다. 지속적인 리서치와 실험을 통해 데이터 과학 프로젝트의 효율성을 극대화할 수 있는 새로운 접근방식을 탐색하고 적용합니다.""",
    },

    'Influence': {
        1: """
#### Individual: 개인의 전문성을 바탕으로 특정 데이터 과학 프로젝트나 서브 시스템에 영향을 미칩니다

* 개인이 보유한 데이터 과학 기술과 지식을 활용하여 프로젝트의 성공에 기여하며, 특정 분석 모델이나 데이터 처리 시스템의 개선을 주도합니다. 이러한 기여는 프로젝트의 결과물 품질을 높이고, 팀 내에서의 전문성을 인정받게 만듭니다.""",
        2: """
#### Team: 데이터 과학 팀 전체에 걸쳐 영향을 끼치며, 팀의 성과와 역량 강화에 기여합니다

* 데이터 과학 분야에서의 깊은 지식과 경험을 팀원들과 공유하며, 팀 전체의 데이터 분석 및 모델링 역량을 향상시킵니다. 협업과 지식 공유를 통해 팀의 전반적인 성과를 높이고, 팀 내 혁신과 성장을 촉진합니다.""",
        3: """
#### Platform: 단일 팀을 넘어 여러 팀 및 플랫폼 전반에 걸쳐 영향을 미치며, 조직의 데이터 과학 전략에 기여합니다

* 조직 내 다양한 데이터 과학 팀과 협업하여, 데이터 기반의 의사결정 프로세스를 강화하고, 조직 전반의 데이터 과학 역량을 향상시킵니다. 이는 조직의 데이터 분석 및 모델링 플랫폼의 발전과 혁신에 중요한 역할을 합니다.""",
        4: """
#### Engineering: 엔지니어링 전체 조직에 영향을 미치며, 여러 데이터 과학 및 엔지니어링 팀 간의 협력을 촉진합니다

* 데이터 과학의 범위를 넘어 엔지니어링 조직 전체에 걸쳐 협업과 지식 공유를 촉진하며, 다학제 간의 프로젝트에서 중추적인 역할을 수행합니다. 이는 기술 및 엔지니어링 분야에서의 혁신과 효율성 증대에 기여합니다.""",
        5: """
#### Company: 기술 조직 뿐만 아니라 비기술 조직을 포함한 전체 회사에 영향을 미칩니다

* 데이터 과학의 영향력을 회사 전체로 확장하여, 비기술 부서를 포함한 조직 전반의 데이터 기반 문화를 강화합니다. 데이터 과학을 통해 얻은 인사이트와 솔루션이 회사의 전략적 의사결정 과정에 중요한 역할을 하며, 비즈니스의 성장과 혁신을 이끕니다.

""",
    },

}


ds_level_stats = {
    'Data Scientist': {
        3: {
            'Technology': 1,
            'System': 1,
            'People': 1,
            'Process': 1,
            'Influence': 1
        },
        4: {
            'Technology': 2,
            'System': 2,
            'People': 2,
            'Process': 1,
            'Influence': 2

        },
        5: {
            'Technology': 3,
            'System': 4,
            'People': 3,
            'Process': 2,
            'Influence': 2

        },
        6: {
            'Technology': 4,
            'System': 4,
            'People': 3,
            'Process': 3,
            'Influence': 3
        },
    },
    'Tech Lead': {
        5: {
            'Technology': 3,
            'System': 4,
            'People': 4,
            'Process': 3,
            'Influence': 2
        },
        6: {
            'Technology': 4,
            'System': 5,
            'People': 4,
            'Process': 4,
            'Influence': 3

        },
        7: {
            'Technology': 5,
            'System': 5,
            'People': 4,
            'Process': 5,
            'Influence': 4

        },
        8: {
            'Technology': 5,
            'System': 5,
            'People': 4,
            'Process': 5,
            'Influence': 5
        },
    },
    'Engineering Manager': {
        5: {
            'Technology': 3,
            'System': 3,
            'People': 4,
            'Process': 4,
            'Influence': 2
       },
        6: {
            'Technology': 4,
            'System': 4,
            'People': 5,
            'Process': 5,
            'Influence': 3

        },
        7: {
            'Technology': 4,
            'System': 4,
            'People': 5,
            'Process': 5,
            'Influence': 4

        },
        8: {
            'Technology': 4,
            'System': 4,
            'People': 5,
            'Process': 5,
            'Influence': 5
        },
    },
}


levels = {
    'Technology': 0,
    'System': 0,
    'People': 0,
    'Process': 0,
    'Influence': 0
}


radar_chart = RadarChart(categories, levels, yticks_labels)
# Generate and save the chart as a PNG file
pic_file_loc = f'charts/template.png'
radar_chart.create_chart(pic_file_loc)

readme_navigator = "#### [README](README.md)"

for job, val in ds_level_stats.items():
    for level, stats in val.items():
        position = f'{job} {level}'
        out_file_loc = f'{position}.md'

        readme_navigator += f"""
* [{position}]({out_file_loc})"""


for job, val in ds_level_stats.items():
    if job == 'Data Scientist':
        area_color = 'orange'
    elif job == 'Tech Lead':
        area_color = 'mediumturquoise'
    else:
        area_color = 'crimson'

    for level, stats in val.items():
        levels = stats
        # Create a RadarChart instance with the categories, levels, and custom y-ticks
        radar_chart = RadarChart(categories, levels, yticks_labels, area_color)
        # Generate and save the chart as a PNG file
        position = f'{job} {level}'
        pic_file_loc = f'charts/{position}.png'
        radar_chart.create_chart(pic_file_loc)

        jb_specific = f"""
{readme_navigator}
<picture>
  <img alt="Template Chart" src="{pic_file_loc}">
</picture>

        """
        for k, v in stats.items():
            jb_specific += f"""
### {k}
            """
            jb_specific += datascience_desc[k][v]
        jb_specific += f"""
{readme_navigator}"""

        out_file_loc = f'{position}.md'
        with open(out_file_loc, 'w') as f:
            f.write(jb_specific)


readme = f"""
# Data Science Ladders
<picture>
  <img alt="Template Chart" src="charts/template.png">
</picture>

{readme_navigator}
"""

readme += f"""

{axes_desc}

## Levels - Level을 결정하는 요소에 대한 설명

"""

for cat in categories:
    readme += f"""
### {cat}
    """
    for lvl in datascience_desc[cat]:
        readme += f"""
{datascience_desc[cat][lvl]}
"""

readme += readme_navigator

with open('README.md', 'w') as f:
    f.write(readme)

